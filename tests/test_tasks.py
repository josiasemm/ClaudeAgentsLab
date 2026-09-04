from src.tasks import create_task, find_task, complete_task


def test_create_task():
    task = create_task("Aprender Claude Code")

    assert task["title"] == "Aprender Claude Code"
    assert task["completed"] is False


def test_find_task():
    tasks = [
        {"id": 1, "title": "Tarea 1", "completed": False},
        {"id": 2, "title": "Tarea 2", "completed": False},
    ]

    task = find_task(tasks, 1)

    assert task["title"] == "Tarea 1"


def test_complete_task():
    tasks = [
        {"id": 1, "title": "Tarea 1", "completed": False},
    ]

    task = complete_task(tasks, 1)

    assert task["completed"] is True
