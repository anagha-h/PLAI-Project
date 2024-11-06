import matplotlib.pyplot as plt
import numpy as np
import random
from datetime import datetime

def generate_random_gridworld(grid_size=5, num_obstacles=2, save_path="gridworld.png"):
    # Initialize an empty grid with zeros
    grid = np.zeros((grid_size, grid_size), dtype=int)

    # Randomly place the robot, goal, and obstacles
    robot_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    grid[robot_pos] = 1  # Mark robot position with 1

    goal_pos = robot_pos
    while goal_pos == robot_pos:  # Ensure goal is not in the same position as robot
        goal_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    grid[goal_pos] = 2  # Mark goal position with 2

    # Place obstacles
    obstacles = set()
    while len(obstacles) < num_obstacles:
        obstacle_pos = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
        if obstacle_pos != robot_pos and obstacle_pos != goal_pos:
            grid[obstacle_pos] = -1  # Mark obstacle position with -1
            obstacles.add(obstacle_pos)

    # Output grid coordinates to the console
    print("Robot position:", robot_pos)
    print("Goal position:", goal_pos)
    print("Obstacle positions:", list(obstacles))

    # Save grid coordinates to a text file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{save_path.replace('.png', '')}_{timestamp}"
    with open(f"{filename}.txt", "w") as f:
        f.write(f"Robot position: {robot_pos}\n")
        f.write(f"Goal position: {goal_pos}\n")
        f.write("Obstacle positions:\n")
        for pos in obstacles:
            f.write(f"{pos}\n")
    print(f"Grid coordinates saved as: {filename}.txt")

    # Visualize the grid
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Draw each cell with colors and labels
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x, y] == 1:
                # Robot cell with a blue background
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color='blue', edgecolor='black', linewidth=2))
                ax.text(y + 0.5, x + 0.5, 'R', ha='center', va='center', color='white', fontsize=15, fontweight='bold')
            elif grid[x, y] == 2:
                # Goal cell with a red background
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color='red', edgecolor='black', linewidth=2))
                ax.text(y + 0.5, x + 0.5, 'G', ha='center', va='center', color='white', fontsize=15, fontweight='bold')
            elif grid[x, y] == -1:
                # Obstacle cell with a black background
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color='black', edgecolor='black', linewidth=2))
            else:
                # Empty cell with white background and black border
                ax.add_patch(plt.Rectangle((y, x), 1, 1, color='white', edgecolor='black', linewidth=2, linestyle='-'))

    # Draw horizontal and vertical grid lines for visibility
    for i in range(grid_size + 1):
        ax.plot([0, grid_size], [i, i], color="black", linewidth=2)  # Horizontal lines
        ax.plot([i, i], [0, grid_size], color="black", linewidth=2)  # Vertical lines

    # Set grid limits and aspect ratio
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_aspect('equal')

    # Remove ticks and labels for a cleaner look
    plt.xticks([])
    plt.yticks([])
    plt.gca().invert_yaxis()

    # Save the plot as a PNG file
    plt.savefig(f"{filename}.png", format="png", dpi=300, bbox_inches='tight')
    plt.show()

    print(f"Gridworld image saved as: {filename}.png")

# Generate and save a random gridworld along with coordinates in a text file
generate_random_gridworld()