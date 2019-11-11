#!/bin/sh

set -e

npx sequelize db:migrate

npm start
