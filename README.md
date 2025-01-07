<h1 align="center">Проект автоматизации тестирования сайта компании HELIX</h1>

# Описание

### Кейсы:
- Проверка смены города
- Наличие вкладки 'Еще' в хедер
- Наличие вкладки 'Сервисы' в хедере
- Наличие вкладки 'Сервисы' в хедере
- Наличие вкладки 'Helixbook' в хедере
- Наличие вкладки 'Адреса Центров Хеликс' в хедере
- Наличие вкладки 'Скидки и акции' в хедере
- Наличие вкладки 'Выезд на дом' в хедере
- Наличие вкладки 'Сдать анализы' в хедере

### Используемый стек технологий и инструментов:

| Python                                                | Pycharm                                                | Git                                                | Pytest                                                | Selene                                                | Allure <br/> Report                                   | Allure <br/> TestOps                                          | Jenkins                                                | Jira                                                |                                                Telegram |
|:------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------|--------------------------------------------------------|-----------------------------------------------------|--------------------------------------------------------:|
| <img height="50" src="source/Python.png" width="50"/> | <img height="50" src="source/Pycharm.png" width="50"/> | <img height="50" src="source/git.svg" width="50"/> | <img height="50" src="source/Pytest.png" width="50"/> | <img height="50" src="source/Selene.png" width="50"/> | <img height="50" src="source/allure.svg" width="50"/> | <img height="50" src="source/allure-testops.png" width="50"/> | <img height="50" src="source/Jenkins.svg" width="50"/> | <img height="50" src="source/Jira.svg" width="50"/> | <img height="50" src="source\Telegram.svg" width="50"/> |



# Запуск тестов c заданными параметрами
```   
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --browser_address=${BROWSER_ADDRESS}
```
# Сборка в Jenkins
Для запуска сборки необходимо перейти в раздел **"Build with Parameters"**, указать адрес браузера и нажать кнопку **"Build"**.

<p align="center">
<img title="Jenkins Build" src="source/build.png"> 
</p>

# Интеграция с Allure
<p align="center">   
<img title="Allure Report" src="source/allure_report.png">    
</p>

# Интеграция с Allure TestOps
<p align="center">   
<img title="Allure TestOps" src="source/allure_testops.png">    
</p>

# Интеграция с Jira
<p align="center">   
<img title="Jira" src="source/jira.png">    
</p>

# Уведомление в Telegram
<p align="center">   
<img title="Telegram" src="source/telegram.png">    
</p>

