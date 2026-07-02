import numpy as np
#1D Array Shape
employee_ages = np.array([22, 25, 28, 31, 35, 40, 27])

print(employee_ages)

print("Shape:", employee_ages.shape)

#2D Array Shape
student_marks = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 91],
    [70, 75, 73]
])

print(student_marks)

print("Shape:", student_marks.shape)

#camera frames 3D question
camera_frames = np.array([
    [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120]
    ],
    [
        [130, 140, 150, 160],
        [170, 180, 190, 200],
        [210, 220, 230, 240]
    ]
])

print("Camera Frames:")
print(camera_frames)

print("\nShape:", camera_frames.shape)

#company sales 3D question
sales = np.array([
    [
        [120, 150, 180, 200],
        [140, 170, 190, 210]
    ],
    [
        [220, 240, 260, 280],
        [230, 250, 270, 290]
    ],
    [
        [320, 340, 360, 380],
        [330, 350, 370, 390]
    ]
])

print("Company Sales:")
print(sales)

print("\nShape:", sales.shape)