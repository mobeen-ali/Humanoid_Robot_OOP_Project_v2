from collections import deque


class TaskManager:
    """
       A class to manage robot tasks using list, stack, and queue data structures.
       Provides logging, undo functionality, and task history.
    """

    def __init__(self):
        self.task_log = []
        self.task_stack = []
        self.task_queue = deque()

    def log_task(self, task):
        """
        Log a task to the task log, stack, and queue.

        Args:
            task (str): Description of the task to log.
        """
        self.task_log.append(task)
        self.task_stack.append(task)
        self.task_queue.append(task)
        print(f"Task Logged: {task}")

    def undo_last_task(self):
        """
        Undo the last task by removing it from the task stack.
        Displays which task is being undone.
        """
        if self.task_stack:
            last_task = self.task_stack.pop()
            print(f"Undoing last task: {last_task}")
        else:
            print("No tasks to undo.")

    def show_logs(self):
        """
        Return a list of all logged tasks.

        Returns:
            list: Task log entries.
        """
        return self.task_log
