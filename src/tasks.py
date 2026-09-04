def create_task(title):
    return {
        "id": 1,
        "title": title,
        "completed": False,
    }


def find_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None


def complete_task(tasks, task_id):
    task = find_task(tasks, task_id)

    task["completed"] = True

    return task


def get_pending_tasks(tasks):
    return [task for task in tasks if task["completed"] is True]
