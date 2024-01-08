mport boto3

def read_file_paths_from_s3(bucket_name, file_key):
    s3 = boto3.client('s3')

    try:
        # Read the contents of the text file
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_contents = response['Body'].read().decode('utf-8')

        # Split the file contents into a list of file paths
        file_paths = file_contents.split('\n')
        file_paths = [path.strip() for path in file_paths if path.strip()]

        return file_paths
    except Exception as e:
        print(f"Error reading file paths from S3: {e}")
        return None
bucket_name = 'healthomicspipeline4'
text_file_key = 'samplesheet.csv'

# Read file paths from the text file
file_paths = read_file_paths_from_s3(bucket_name, text_file_key)