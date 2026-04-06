from workers.celery_app import celery_app

@celery_app.task(bind=True)
def process_pdf_task(self, paper_id: str, file_path: str, subject_id: str):
    """Main background task: full pipeline for one PDF."""
    try:
        self.update_state(state="PROGRESS", meta={"step": "extracting", "progress": 10})
        # TODO: call orchestrator.run_pipeline()
        return {"status": "completed", "paper_id": paper_id}
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60, max_retries=3)

@celery_app.task
def sync_drive_task(folder_id: str):
    """Sync new PDFs from Google Drive folder."""
    # TODO: call drive_watcher
    pass

@celery_app.task
def regenerate_strategy_task(subject_id: str):
    """Regenerate strategy after new paper is processed."""
    # TODO: call strategy_generator for all strategy types
    pass
