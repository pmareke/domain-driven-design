FROM mongo

COPY weathers.json /init.json

CMD mongoimport --drop --host mongo --db weather --collection weather --mode delete --type json --file /init.json --jsonArray


CMD mongoimport --drop --host mongo --db weather --collection weather --type json --file /init.json --jsonArray
