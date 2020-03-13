from unittest import TestCase
from random import randint, choice
from math import factorial
from tempfile import mkdtemp
from shutil import rmtree
from os import path
from date import (is_leap_year,
                  validate_year,
                  validate_month,
                  validate_day,
                  create_all_variations,
                  get_earliest_date,
                  date,
                  )


class IsLeapYearTestCase(TestCase):
    def test_2001(self):
        self.assertFalse(is_leap_year(2001))

    def test_2004(self):
        self.assertTrue(is_leap_year(2004))

    def test_2000(self):
        self.assertTrue(is_leap_year(2000))

    def test_2012(self):
        self.assertTrue(is_leap_year(2012))

    def test_2100(self):
        self.assertFalse(is_leap_year(2100))


class ValidateYearTestCase(TestCase):
    def test_valid_1_or_2_digit_year(self):
        for year in range(0, 100):
            with self.subTest(year=year):
                self.assertTrue(validate_year(year))

    def test_valid_4_digit_year(self):
        for year in range(2000, 3000):
            with self.subTest(year=year):
                self.assertTrue(validate_year(year))

    def test_invalid_year(self):
        self.assertFalse(validate_year(-1))

    def test_invalid_4_digit_year(self):
        self.assertFalse(validate_year(3000))


class ValidateMonthTestCase(TestCase):
    def test_valid_month(self):
        for month in range(1, 13):
            with self.subTest(month=month):
                self.assertTrue(validate_month(month))

    def test_invalid_month(self):
        self.assertFalse(validate_month(0))

    def test_invalid_4_digit_month(self):
        self.assertFalse(validate_month(3000))


class ValidateDayTestCase(TestCase):
    def test_0_as_a_day(self):
        for month in range(1, 13):
            year = randint(2000, 3000)
            with self.subTest(month=month, year=year):
                self.assertFalse(validate_day(year, month, 0))

    def test_valid_day_for_31_days_months(self):
        for month in [1, 3, 5, 7, 8, 10, 12]:
            for day in range(1, 32):
                year = randint(2000, 3000)
                with self.subTest(day=day, month=month, year=year):
                    self.assertTrue(validate_day(year, month, day))

    def test_invalid_day_for_31_days_months(self):
        for month in [1, 3, 5, 7, 8, 10, 12]:
            year = randint(2000, 3000)
            with self.subTest(month=month, year=year):
                self.assertFalse(validate_day(year, month, 32))

    def test_valid_day_for_30_days_months(self):
        for month in [4, 6, 9, 11]:
            year = randint(2000, 2999)
            for day in range(1, 31):
                with self.subTest(day=day, month=month, year=year):
                    self.assertTrue(validate_day(year, month, day))

    def test_invalid_day_for_30_days_months(self):
        for month in [4, 6, 9, 11]:
            year = randint(2000, 3000)
            with self.subTest(month=month, year=year):
                self.assertFalse(validate_day(year, month, 31))

    def test_valid_day_for_february(self):
        year = randint(2000, 2999)
        for day in range(1, 29):
            with self.subTest(day=day, year=year):
                self.assertTrue(validate_day(year, 2, day))

    def test_valid_day_for_february_in_leap_years(self):
        leap_years = [year for year in range(2000, 3000) if is_leap_year(year)]
        for day in range(1, 30):
            year = choice(leap_years)
            with self.subTest(day=day, year=year):
                self.assertTrue(validate_day(year, 2, day))

    def test_invalid_day_for_february_leap_year(self):
        leap_years = [year for year in range(2000, 3000) if is_leap_year(year)]
        for year in leap_years:
            with self.subTest(year=year):
                self.assertFalse(validate_day(year, 2, 30))

    def test_invalid_day_for_february_not_leap_year(self):
        leap_years = [year for year in range(2000, 3000) if is_leap_year(year)]
        for year in [year for year in range(2000, 3000) if year not in leap_years]:
            with self.subTest(year=year):
                self.assertFalse(validate_day(year, 2, 29))


class CreateAllVariationsTestCase(TestCase):
    def test_number_of_variations(self):
        self.assertEqual(len(create_all_variations(0, 3, 14)), factorial(3))

    def test_for_duplicates(self):
        all_variations = create_all_variations(0, 3, 14)
        for variation in all_variations:
            with self.subTest(variation=variation):
                self.assertEqual((all_variations.count(variation)), 1)


class GetEarliestDateTestCase(TestCase):
    def test_get_earliest_date(self):
        self.assertEqual(get_earliest_date([[2001, 12, 21], [2050, 1, 12], [2001, 11, 31]]), [2001, 11, 31])


class DateTestCase(TestCase):
    def setUp(self):
        self.test_dir = mkdtemp(dir='.')

    def tearDown(self):
        rmtree(self.test_dir)

    def test_31_0_1(self):
        f = open(path.join(self.test_dir, 'test.txt'), 'w')
        f.write('31/0/1')
        f.close()
        f = open(path.join(self.test_dir, 'test.txt'))
        self.assertEqual(date(f.name), '2000-01-31')
        f.close()

    def test_12_10_01(self):
        f = open(path.join(self.test_dir, 'test.txt'), 'w')
        f.write('12/10/01')
        f.close()
        f = open(path.join(self.test_dir, 'test.txt'))
        self.assertEqual(date(f.name), '2001-10-12')
        f.close()

    def test_31_31_31(self):
        f = open(path.join(self.test_dir, 'test.txt'), 'w')
        f.write('31/31/31')
        f.close()
        f = open(path.join(self.test_dir, 'test.txt'))
        self.assertEqual(date(f.name), '31/31/31 is illegal')
        f.close()

    def test_a_31_31(self):
        f = open(path.join(self.test_dir, 'test.txt'), 'w')
        f.write('a/31/31')
        f.close()
        f = open(path.join(self.test_dir, 'test.txt'))
        self.assertEqual(date(f.name), None)
        f.close()
