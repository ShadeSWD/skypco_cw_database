from src.vacancy import Vacancy
from src.api.hh_api import HeadHunterAPI
from src.database.DBManager import DBManager


class VacanciesParserApp:
    def __init__(self):
        self.__vacancies: list['Vacancy'] = []
        self.__amount_vacancy: int | None = None
        self.__site_to_parse = HeadHunterAPI()
        self.db_manager = DBManager()

    def interact_with_user(self) -> None:
        """ Взаимодействие с пользователем. """

        while True:
            print("\n1. Поиск вакансий\n2. Отобразить вакансии\n3. Выход")
            choice_menu = input("Выберите действие: ")

            if choice_menu == "1":
                self.search_vacancies()

            elif choice_menu == "2":
                self.display_vacancies()

            elif choice_menu == "3":
                break
            else:
                print("Ошибка ввода")

    def search_vacancies(self) -> None:
        """Собирает вакансии по имеющимся работодателям"""

        while True:
            amount_vacancy = input("\nВведите количество вакансий для поиска в каждой компании: ")
            if amount_vacancy.isdigit():
                self.__amount_vacancy = int(amount_vacancy)
                break
            else:
                print("Ошибка ввода")

        for emp_id in self.db_manager.get_employers().values():
            vacancies = self.__site_to_parse.search_vacancies(employer_id=emp_id,
                                                              number_of_vacancies=self.__amount_vacancy)
            if vacancies:
                self.db_manager.update_vacancies(vacancies)

    def display_vacancies(self) -> None:
        """Отображение вакансий"""

        while True:
            print("\n1. Вывести количество вакансий всех компаний\n2. Отобразить весь список\n3. Отобразить вакансии с "
                  "зарплатой выше средней\n4. Поиск по ключевому слову\n5. Выход")
            choice_menu = input("Выберите действие: ")

            if choice_menu == "1":
                self.count_company_vacancies()

            elif choice_menu == "2":
                self.get_all_vacancies()

            elif choice_menu == "3":
                self.get_vacancies_with_higher_salary()

            elif choice_menu == "4":
                self.get_vacancies_with_keyword()

            elif choice_menu == "5":
                break
            else:
                print("Ошибка ввода")

    def count_company_vacancies(self):
        """Выводит количество вакансий для каждой компании"""
        quantities = self.db_manager.get_companies_and_vacancies_count()
        print('')
        for company, quantity in quantities.items():
            print(f'{company}: {quantity}')

    def get_all_vacancies(self):
        """Выводит все вакансии"""
        vacancies_data = self.db_manager.get_all_vacancies()
        for line in vacancies_data:
            print(f"{line['company_name']} - {line['vacancy_name']} от {line['salary_from']} до {line['salary_to']} "
                  f"{line['url']}")

    def get_vacancies_with_higher_salary(self):
        """Выводит все вакансии с зарплатой выше средней"""
        vacancies_data = self.db_manager.get_vacancies_with_higher_salary()
        print('')
        for line in vacancies_data:
            print(f"{line['company_name']} - {line['vacancy_name']} от {line['salary_from']} до {line['salary_to']} "
                  f"{line['url']}")

    def get_vacancies_with_keyword(self):
        """Получает список всех вакансий, в названии которых содержится ключевое слово"""
        keyword = input("\nВведите ключевое слово: ").strip().lower()
        vacancies_data = self.db_manager.get_vacancies_with_keyword(keyword)
        print('')
        for line in vacancies_data:
            print(f"{line['company_name']} - {line['vacancy_name']} от {line['salary_from']} до {line['salary_to']} "
                  f"{line['url']}")
