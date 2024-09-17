### [Localhost PostgreSQL](https://www.w3schools.com/postgresql/postgresql_getstarted.php)
1. SQL Shell (purely command line)
2. pgAdmin4 - table relation diagrams

### Local python connects to local postgres
1. postgreSQL installation on macos: https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql-macos/
2. pip3 install psycopg2 --break-system-packages
3. Error: pg_config executable not found.
4. here: https://www.geeksforgeeks.org/how-to-fix-pg_config-executable-not-found-in-python
5. pg_config locates at /Library/PostgreSQL/16/bin
6. export PATH=$PATH:/Library/PostgreSQL/16/bin
7. re-run pip3 install psycopg2 --break-system-packages

### Build deployments with postgres image (direct access pod for SQL playground)
1. https://www.digitalocean.com/community/tutorials/how-to-deploy-postgres-to-kubernetes-cluster
2. https://phoenixnap.com/kb/postgresql-kubernetes

### [Posgres DB in Kubernetes with a Python client example](https://kodekloud.com/blog/deploy-postgresql-kubernetes/):
* It mentions that `The hostname of the Postgres Pod. Use the DNS name of the stateful set, which is <statefulset-name>. <headless-service-name>. In our case, it is postgres.postgres.` I've tested it, doesn't seem to work.
* Found the answer from this [article](https://medium.com/@SabujJanaCodes/building-a-golang-music-api-and-deploying-it-on-k8s-go-mysql-k8s-841612d13479) even though it is demostrating Go and MySQL in different namespaces of Kubernetes.

#### This [article](https://medium.com/@SabujJanaCodes/building-a-golang-music-api-and-deploying-it-on-k8s-go-mysql-k8s-841612d13479) is very GOOD! Need more study:
1. `k get po -n ps-ns -owide`, IP column OR `k get endpoints -n ps-ns`, and if I sue the IP address for the host variable in the code, it also works. But that step shouldn't be needed in reality.
2. it covers go interface and json implementation.

#### [Another Golang/PostgreSQL on Kubernetes example](https://levelup.gitconnected.com/deploying-dockerized-golang-api-on-kubernetes-with-postgresql-mysql-d190e27ac09f):
1. Need to follow, last time wasn't working

#### [What is hostNetwork in Kubernetes?](https://stackoverflow.com/questions/77110555/what-is-hostnetwork-in-kubernetes)
- If that is set to true, then the app inside the pod will use the localhost address of its host (my macbook local), instead of the container's localhost.

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