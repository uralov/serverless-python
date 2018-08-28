# serverless-python
Application performance comparison Django vs Flask vs Native lambda using [serverless framework](https://serverless.com/framework/) in [AWS Lambda](https://aws.amazon.com/lambda/).

## Results:
### Native lambda
**Size**: Uploading service .zip file to S3 (3.84 MB)...
**Cold start:** Duration: 1.60 ms	Billed Duration: 100 ms Memory Size: 1024 MB	Max Memory Used: 34 MB	
**After warm-up:** Duration: 1.19 - 3 ms	Billed Duration: 100 ms Memory Size: 1024 MB	Max Memory Used: 34 MB	

### Flask
**Size**: Uploading service .zip file to S3 (6.91 MB)...
**Cold start:** Duration: 290.83 ms	Billed Duration: 300 ms Memory Size: 1024 MB	Max Memory Used: 67 MB
**After warm-up:** Duration: 3.97 - 20 ms	Billed Duration: 100 ms Memory Size: 1024 MB	Max Memory Used: 67 MB

### Django
**Size**: Uploading service .zip file to S3 (14.47 MB)...
**Cold start:** Duration: 675.96 ms	Billed Duration: 700 ms Memory Size: 1024 MB	Max Memory Used: 71 MB
**After warm-up:** Duration: 11.33 - 70 ms	Billed Duration: 100 ms Memory Size: 1024 MB	Max Memory Used: 71 MB	
