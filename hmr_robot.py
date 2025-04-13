from hmr_battery import Battery
from hmr_environment import Environment
from hmr_task_manager import TaskManager


class Robot:
    """
        A class representing a humanoid robot with capabilities to move,
        handle objects, manage battery, log tasks, and shut down.
    """
    def __init__(self):
        """Initialize the robot with default position, battery, and task management."""
        self.x = 0
        self.y = 0
        self.holding_object = None
        self.battery = Battery()
        self.environment = Environment()
        self.task_manager = TaskManager()
        self.is_active = True  # Robot starts active

    def move(self, direction):
        """
        Move the robot in a specified direction (forward/backward).

        Args:
            direction (str): Direction to move ('forward' or 'backward').
        """
        if not self.is_active:
            print("Robot is shut down. Cannot move.")
            return

        if self.battery.charge <= 10:
            print("Battery too low to move. Please recharge.")
            return

        if self.environment.detect_obstacle():
            print("Obstacle detected! Movement blocked.")
            return

        if direction.lower() == "forward":
            self.y += 1
        elif direction.lower() == "backward":
            self.y -= 1

        self.battery.drain(5)  # Drain battery by 5%
        self.task_manager.log_task(f"Moved {direction} to ({self.x}, {self.y})")
        print(f"Robot moved {direction}. New position: ({self.x}, {self.y})")

    def pick_up(self, item):
        """
        Pick up an item if not already holding one.

        Args:
            item (str): The item to be picked up.
        """
        if not self.is_active:
            print("Robot is shut down. Cannot pick up objects.")
            return

        if self.holding_object:
            print("Cannot pick up object. Drop the current object first.")
        else:
            self.holding_object = item
            self.task_manager.log_task(f"Picked up {item}")
            print(f"Picked up {item}")

    def drop(self):
        """Drop the currently held object, if any."""
        if not self.is_active:
            print("Robot is shut down. Cannot drop objects.")
            return

        if self.holding_object:
            print(f"Dropped {self.holding_object}")
            self.task_manager.log_task(f"Dropped {self.holding_object}")
            self.holding_object = None
        else:
            print("No object to drop.")

    def check_battery(self):
        """Print the current battery level."""
        if not self.is_active:
            print("Robot is shut down. Cannot check battery.")
            return

        battery_status = self.battery.check_battery()
        print(battery_status)

    def recharge(self):
        """Recharge the robot's battery to full."""
        if not self.is_active:
            print("Robot is shut down. Cannot recharge.")
            return

        self.battery.recharge()
        self.task_manager.log_task("Recharged battery")
        print("Battery fully recharged.")

    def shutdown(self):
        """Shut down the robot, disabling all further operations."""
        self.is_active = False
        self.task_manager.log_task("Robot has been shut down")
        print("Robot is now shut down.")

    def execute_last_task(self):
        """Undo the last task using the task manager's stack."""
        if not self.is_active:
            print("Robot is shut down. Cannot execute tasks.")
            return

        self.task_manager.undo_last_task()
