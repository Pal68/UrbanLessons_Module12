import unittest as ut
import runner

class RunnerTest(ut.TestCase):
    def test_walk(self):
        runner_obj = runner.Runner('Vasya')
        for i in range(0,10):
            runner_obj.walk()
        self.assertEqual(runner_obj.distance, 50)

    def test_run(self):
        runner_obj = runner.Runner('Vasya')
        for i in range(0,10):
            runner_obj.run()
        self.assertEqual(runner_obj.distance, 100)

    def test_challenge(self):
        runner_obj1 = runner.Runner('Vasya')
        runner_obj2 = runner.Runner('Fedya')
        for i in range(0,10):
            runner_obj1.run()
            runner_obj2.walk()
        self.assertNotEqual(runner_obj1.distance, runner_obj2.distance)

if __name__ == "__main__":
    ut.main