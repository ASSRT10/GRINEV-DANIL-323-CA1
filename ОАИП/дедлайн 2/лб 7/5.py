def format_report(report_title: str, *data: str, **properties: str) -> None:
    """
    Форматирует и выводит отчёт с заголовком, данными и свойствами.
    Parameters:
    report_title: str - заголовок отчёта
    *data: str - произвольное количество пунктов отчёта
    **properties: str - метаданные отчёта (автор, дата и т.д.)
    """
    print(f"-- Отчет: {report_title} --")
    print("Данные:")
    if data:
        for item in data:
            print(f"   - {item}")
    else:
        print("   Нет данных")
    print("\nСвойства:")
    if properties:
        for key, value in properties.items():
            print(f"   - {key}: {value}")
    else:
        print("   Нет свойств")
format_report(
    "Ежедневный отчет",
    "Продажи выросли на 10%",
    "Новых клиентов: 5",
    author="Сидоров А.В.",
    date="2025-11-04"
)