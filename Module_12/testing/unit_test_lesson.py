import unittest
from main import Student


class TestStudent(unittest.TestCase):
    def test_walk_distance(self):
        student = Student("Walker")
        for _ in range(10):
            student.walk()

        self.assertEqual(student.distance, 50, f"Дистанции не равны {student.distance} != 50")
        # self.assertEqual(student.distance, 500, f"Дистанции не равны {student.distance} != 500")

    def test_runner_distance(self):
        student = Student("Runner")
        for _ in range(10):
            student.run()

        self.assertEqual(student.distance, 100, f"Дистанции не равны {student.distance} != 100")
        # self.assertEqual(student.distance, 1000, f"Дистанции не равны {student.distance} != 1000")

    def test_competition(self):
        runner = Student("Runner")
        walker = Student("Walker")
        for _ in range(10):
            runner.run()
            walker.walk()

        self.assertGreater(
            runner.distance,
            walker.distance,
            f"{runner.name} должен преодолеть дистанцию больше, чем {walker.name}"
        )

        # self.assertLess(
        #     runner.distance,
        #     walker.distance,
        #     f"{runner.name} должен преодолеть дистанцию больше, чем {walker.name}"
        # )


if __name__ == '__main__':
    unittest.main()
