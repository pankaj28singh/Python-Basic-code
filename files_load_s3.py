import boto3
import logging

aws_access_key_id='AKIAI3UZLKCPUJU7MGOA' 
aws_secret_access_key='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'

#logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='app.log', filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
def main():
	
	logging.info('Program start')
	logging.info('Now boto connection is created')
	s3 = boto.client('s3',aws_access_key_id='AKIAI3UZLKCPUJU7MGOA', aws_secret_access_key='+Z7msy9hiJGg58XkPusRqShc7/AOZ9gP72GMg1m/')
	logging.info('we are downloading')
	s3.download_file('deepak-karuna','samples3.csv','rithvik3.csv')
	logging.info('Application done')



if __name__== "__main__":
	
	logging.info("Program in mainfunctions")
	main()