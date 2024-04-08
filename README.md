#### command line query
```
/Library/PostgreSQL/16 
$ find . -name psql
./debug_symbols/bin/psql.dSYM/Contents/Resources/DWARF/psql
./debug_symbols/pgAdmin4.app/Contents/Resources/web/pgadmin/tools/psql
./debug_symbols/pgAdmin4.app/Contents/SharedSupport/psql.dSYM/Contents/Resources/DWARF/psql
./bin/psql
./pgAdmin 4.app/Contents/Resources/web/pgadmin/tools/psql
./pgAdmin 4.app/Contents/SharedSupport/psql
find: ./data: Permission denied
/Library/PostgreSQL/16 
$ ./bin/psql -U postgres -d postgres -c 'SELECT * FROM person' 
Password for user postgres: 
 id | name | age | gender 
----+------+-----+--------
  1 | Mike |  30 | m
  2 | Lisa |  25 | f
  3 | Leo  |  40 | m
(3 rows)
```
