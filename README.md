# serverless-python
Application performance comparison Django vs Flask vs Native lambda using [serverless framework](https://serverless.com/framework/) in [AWS Lambda](https://aws.amazon.com/lambda/).

## Results:

| Framework     | Pack size | Memory usage | Cold start | After warm-up |
|---------------|-----------|--------------|------------|---------------|
| Native lambda | 3.84 MB   | 34 MB        | 1.60 ms    | 1.19 - 3 ms   |
| Flask         | 6.91 MB   | 67 MB        | 290.83 ms  | 3.97 - 20 ms  |
| Django        | 14.47 MB  | 71 MB        | 675.96 ms  | 11.33 - 70 ms |
