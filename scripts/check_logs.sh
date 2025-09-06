#!/bin/bash
# Проверка логов на ошибки
grep "ERROR" /var/log/syslog > error_logs.txt
echo "Ошибки сохранены в error_logs.txt"
