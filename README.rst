=================================
Twitter Bot Popularity Evaluation
=================================


.. image:: https://img.shields.io/pypi/v/twitter_bot_popularity_evaluation.svg
        :target: https://pypi.python.org/pypi/twitter_bot_popularity_evaluation

.. image:: https://img.shields.io/travis/DatenkrakeWasTaken/twitter_bot_popularity_evaluation.svg
        :target: https://travis-ci.com/DatenkrakeWasTaken/twitter_bot_popularity_evaluation

.. image:: https://readthedocs.org/projects/twitter-bot-popularity-evaluation/badge/?version=latest
        :target: https://twitter-bot-popularity-evaluation.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/DatenkrakeWasTaken/twitter_bot_popularity_evaluation/shield.svg
     :target: https://pyup.io/repos/github/DatenkrakeWasTaken/twitter_bot_popularity_evaluation/
     :alt: Updates



Twitter-Bot zur Auswertung der Beliebtheit von zwei verschiedenen Themen, in diesem Fall Katzen und Hunde.


* Free software: MIT license


Dokumentation
--------

Diese Anwendung bietet die Möglichkeit aufbereiteten Content für zwei unterschiedliche Accounts über einen beliebig langen Zeitraum automatisiert zu tweeten. 

**Voraussetzungen:**

* Zugriff auf Twitter-API
* CSV-Datei mit folgenden Spalten: „image“ (enthält Dateinamen der Bilder die getweeted werden sollen), „text“ (enthält Text welcher in Tweet enthalten sein soll) und „hashtags“
* Bilder, die getweeted werden sollen

**Vorbereitung & Ausführung:**

* API Keys, Secrets und Tokens in GitHub Secrets eintragen
* In „/.github/workflows/main.yml“ die gewünschte Zeit zum automatisierten tweeten eintragen
* Die Bilder in „content/cats/images/“ und „content/dogs/images/“ hochladen.
* Aufbereitete CSV-Dateien mit Tweet-Inhalten in „content/cats/“ und „content/dogs/“ hochladen
* In „scripts/data_structure.ipynb“ die Parameter anpassen („days_to_post“, „posts_per_day“, „starting_date“)
* „scripts/data_structure.ipynb“ ausführen
* In „ /scripts/post.py“ User Ids der Accounts anpassen („user_id_dog“ und „user_id_cat“)
* Nach dem befolgen dieser Schritte wird nun täglich der aufbereitete Content den Parametern entsprechend getweeted

**Optional:**

* Optional kann „ /scripts/renaming_images.ipynb“ ausgeführt werden, wodurch die Bilder umbenannt werden zu „1.jpg“, „2.jpg“, „3.jpg“… wodurch das Eintragen der Dateinamen in die CSV-Datei erleichtert wird.

**Einschränkungen:**

* Aktuell können nur ein oder zwei Tweets pro Tag getweeted werden
* Es muss auf zwei Accounts getweeted werden
* Ein Tweet muss ein Bild enthalten, ein Text hingegen ist optional

Durch Anpassung der Skripte können diese Einschränkungen aufgehoben oder auf die jeweiligen Bedürfnisse des Users angepasst werden.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
