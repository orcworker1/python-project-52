[![SonarQube Cloud](https://sonarcloud.io/images/project_badges/sonarcloud-light.svg)](https://sonarcloud.io/summary/new_code?id=orcworker1_python-project-52)
[![Actions Status](https://github.com/orcworker1/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/orcworker1/python-project-52/actions)
<h1>Render:
  https://python-project-52-b0ra.onrender.com


<body>
<h1>Production Build (Product)</h1>

<h2>Используется</h2>
<ul>
<li>Python 3.11+</li>
<li>PostgreSQL 15+</li>
<li> Django 5.2 </li>
<li><a href="https://github.com/astral-sh/uv" target="_blank">uv</a> — менеджер пакетов</li>
</ul>

<h2>Установка и запуск</h2>
<p>Клонируйте репозиторий:</p>
<pre><code>git clone https://github.com/orcworker1/python-project-52.git
cd python-project-52</code></pre>

<p>Установите зависимости:</p>
<pre><code>make install</code></pre>

<h2>Создайте файл .env</h2>
<pre><code>SECRET_KEY=your_secret_key
DEBUG=True # Set to False in production
DATABASE_URL=postgresql://username:password@localhost:5432/dbname</code></pre>
<p>Замените <code>username</code>, <code>password</code>, <code>dbname</code> и <code>your_secret_key</code> на свои значения.</p>

<h2>Сборка и запуск приложения</h2>
<pre><code>make build
make start</code></pre>

<p><strong>Примечание:</strong> В продакшене установите <code>DEBUG=False</code> и используйте надёжные учётные данные для базы данных.</p>
</body>
</html>
