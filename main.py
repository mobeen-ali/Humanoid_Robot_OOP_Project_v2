from hmr_robot import Robot


def main():
    """
    Main function to run the command-line interface for the humanoid robot.
    Users can input commands to control the robot's actions.
    """
    robot = Robot()

    while True:
        print("\nCommands: move [forward/backward], pick_up [item], drop, check_battery, recharge, shutdown, undo, "
              "logs, exit")
        command = input("Enter command: ").strip().lower()

        if command.startswith("move"):
            _, direction = command.split(maxsplit=1)
            robot.move(direction)
        elif command.startswith("pick_up"):
            _, item = command.split(maxsplit=1)
            robot.pick_up(item)
        elif command == "drop":
            robot.drop()
        elif command == "check_battery":
            robot.check_battery()
        elif command == "recharge":
            robot.recharge()
        elif command == "shutdown":
            robot.shutdown()
            break  # Stops the loop
        elif command == "undo":
            robot.execute_last_task()
        elif command == "logs":
            logs = robot.task_manager.show_logs()
            print("\nTask Logs:")
            for log in logs:
                print(f"- {log}")
        elif command == "exit":
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
