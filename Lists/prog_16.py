'''
This advanced program finds the correct order in which project tasks should be completed.
A task cannot start until its dependencies are completed.
'''
def create_task_schedule(
    tasks: list[dict]
) -> list[str]:

    task_ids = []

    for task in tasks:
        task_ids.append(task["task_id"])

    dependency_count = {}
    dependent_tasks = {}

    for task_id in task_ids:
        dependency_count[task_id] = 0
        dependent_tasks[task_id] = []

    for task in tasks:
        task_id = task["task_id"]

        for dependency in task["dependencies"]:
            if dependency not in task_ids:
                raise ValueError(
                    f"Unknown dependency: {dependency}"
                )

            dependent_tasks[dependency].append(task_id)
            dependency_count[task_id] += 1

    available_tasks = []

    for task_id in task_ids:
        if dependency_count[task_id] == 0:
            available_tasks.append(task_id)

    final_schedule = []
    current_index = 0

    while current_index < len(available_tasks):
        completed_task = available_tasks[
            current_index
        ]

        current_index += 1

        final_schedule.append(completed_task)

        for dependent_task in dependent_tasks[
            completed_task
        ]:
            dependency_count[dependent_task] -= 1

            if dependency_count[dependent_task] == 0:
                available_tasks.append(
                    dependent_task
                )

    if len(final_schedule) != len(tasks):
        raise ValueError(
            "Circular dependency detected. "
            "The project schedule cannot be created."
        )

    return final_schedule


project_tasks = [
    {
        "task_id": "Requirements",
        "dependencies": []
    },
    {
        "task_id": "Database Design",
        "dependencies": ["Requirements"]
    },
    {
        "task_id": "UI Design",
        "dependencies": ["Requirements"]
    },
    {
        "task_id": "Backend Development",
        "dependencies": ["Database Design"]
    },
    {
        "task_id": "Frontend Development",
        "dependencies": ["UI Design"]
    },
    {
        "task_id": "Integration",
        "dependencies": [
            "Backend Development",
            "Frontend Development"
        ]
    },
    {
        "task_id": "Testing",
        "dependencies": ["Integration"]
    },
    {
        "task_id": "Deployment",
        "dependencies": ["Testing"]
    }
]

try:
    schedule = create_task_schedule(project_tasks)

    print("PROJECT EXECUTION SCHEDULE")
    print("=" * 60)

    for position, task in enumerate(
        schedule,
        start=1
    ):
        print(f"{position}. {task}")

except ValueError as error:
    print(f"Scheduling error: {error}")
