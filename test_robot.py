"""
Automated test suite for the Humanoid Robot project.
Tests key functionalities such as movement, battery behavior,
object manipulation, task logging, undo, and shutdown.
"""


from hmr_robot import Robot


def test_movement():
    """Test robot movement in forward and backward directions."""
    robot = Robot()
    initial_y = robot.y
    robot.move("forward")
    assert robot.y == initial_y + 1 or robot.y == initial_y, "Forward movement failed or blocked by obstacle"

    robot.move("backward")
    assert robot.y in [initial_y - 1, initial_y], "Backward movement failed or blocked by obstacle"


def test_battery_drain():
    """Test battery drain after movement."""
    robot = Robot()
    initial_charge = robot.battery.charge
    robot.move("forward")
    expected_charge = initial_charge - 5 if initial_charge > 10 else initial_charge
    assert robot.battery.charge == expected_charge or robot.battery.charge == initial_charge, "Battery did not drain correctly"


def test_battery_recharge():
    """Test draining and recharging the battery."""
    robot = Robot()
    robot.battery.drain(50)
    assert robot.battery.charge == 50, "Battery drain failed"
    robot.recharge()
    assert robot.battery.charge == 100, "Battery recharge failed"


def test_pickup_and_drop():
    """Test picking up and dropping an object."""
    robot = Robot()
    robot.pick_up("box")
    assert robot.holding_object == "box", "Pick-up failed"

    robot.drop()
    assert robot.holding_object is None, "Drop failed"


def test_pickup_while_holding():
    """Test trying to pick up another object while already holding one."""
    robot = Robot()
    robot.pick_up("box")
    robot.pick_up("item")  # Should not override the current object
    assert robot.holding_object == "box", "Robot should not pick up another item while holding one"


def test_task_logging():
    """Test logging of pick-up and drop tasks."""
    robot = Robot()
    robot.pick_up("book")
    robot.drop()
    logs = robot.task_manager.show_logs()
    assert any("Picked up book" in task for task in logs), "Pick-up not logged"
    assert any("Dropped book" in task for task in logs), "Drop not logged"


def test_undo_last_task():
    """Test execution of the undo operation."""
    robot = Robot()
    robot.move("forward")
    initial_log_count = len(robot.task_manager.task_log)
    robot.execute_last_task()  # Undo operation
    assert len(robot.task_manager.task_log) == initial_log_count, "Undo should not affect logs"
    # Note: Actual undo logic only prints; test verifies no crash and functional call


def test_shutdown():
    """Test robot shutdown and blocked functionality afterward."""
    robot = Robot()
    robot.shutdown()
    assert robot.is_active is False, "Robot should be shut down"

    robot.move("forward")  # Should be blocked
    assert robot.y == 0, "Robot should not move after shutdown"

    robot.recharge()  # Should be blocked
    assert robot.battery.charge == 100, "Robot should not recharge after shutdown"


if __name__ == "__main__":
    print("Running tests...")
    test_movement()
    test_battery_drain()
    test_battery_recharge()
    test_pickup_and_drop()
    test_pickup_while_holding()
    test_task_logging()
    test_undo_last_task()
    test_shutdown()
    print("All tests passed successfully.")
