math_students = {"Alice", "Bob", "Charlie", "David"}
physics_students = {"Bob", "David", "Eve", "Frank"}
cs_students = {"Alice", "Charlie", "Eve", "Grace"}
all_three = math_students & physics_students & cs_students
only_one = (math_students - physics_students - cs_students) | \
(physics_students - math_students - cs_students) | \
(cs_students - math_students - physics_students)
math_not_physics = math_students - physics_students
total_students = math_students | physics_students | cs_students
print(f"Все три курса: {all_three}")
print(f"Только один курс: {only_one}")
print(f"Математика но не физика: {math_not_physics}")
print(f"Всего студентов: {len(total_students)}")
print(f"Все студенты: {total_students}")