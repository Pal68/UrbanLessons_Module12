import unittest as ut
import runner

class TournamentTest(ut.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner.Runner('Усейн', 10)
        self.runner2 = runner.Runner('Андрей', 9)
        self.runner3 = runner.Runner('Ник', 3)
        pass

    @classmethod
    def tearDownClass(cls):
        # print(cls.all_results)
        for k, v in cls.all_results.items():
            result_dict = {}
            s = ''
            for k1, v1 in v.items():
                s = s + f'{k1}:{v1}'
                result_dict.update({k1 : v1.name})
            print(result_dict)

    def test_run_1(self):
        tournament = runner.Tournament(90,self.runner1, self.runner3)
        result = tournament.start()
        cls = self.__class__
        cls.all_results['test_run_1'] = result
        last_runner = result[max(result)].name
        self.assertTrue(last_runner == 'Ник')

    def test_run_2(self):
        tournament = runner.Tournament(90,self.runner2, self.runner3)
        result = tournament.start()
        cls = self.__class__
        cls.all_results ['test_run_2'] = result
        last_runner = result[max(result)].name
        self.assertTrue(last_runner == 'Ник')

    def test_run_3(self):
        tournament = runner.Tournament(90,self.runner1, self.runner2, self.runner3)
        result = tournament.start()
        cls = self.__class__
        cls.all_results ['test_run_3'] = result
        last_runner = result[max(result)].name
        self.assertTrue(last_runner == 'Ник')



if __name__ == '__main__':
    ut.main
