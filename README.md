# serverless-python
Application performance comparison Django vs Flask vs Native lambda using [serverless framework](https://serverless.com/framework/) in [AWS Lambda](https://aws.amazon.com/lambda/).

## Results:

### Framework comparison 
| Framework     | Pack size | Memory usage | Cold start | After warm-up |
|---------------|-----------|--------------|------------|---------------|
| Native lambda | 3.84 MB   | 34 MB        | 1.60 ms    | 1.19 - 3 ms   |
| Flask         | 6.91 MB   | 67 MB        | 290.83 ms  | 3.97 - 20 ms  |
| Django        | 14.47 MB  | 71 MB        | 675.96 ms  | 11.33 - 70 ms |

### ORM comparison 
| ORM         | Memory usage | Cold start | After warm-up  |
|-------------|--------------|------------|----------------|
| Psycopg2    | 59 MB        | 2.96 ms    | 1.59 - 1.6 ms  |
| SQL Alchemy | 58 MB        | 37.60 ms   | 2.31 - 2.49 ms |
| Peewee      | 58 MB        | 16.65 ms   | 3.89 - 4.2 ms  |
| Django ORM  | 54 MB        | 297.40 ms  | 2.15 - 2.26 ms |
