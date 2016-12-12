import unirest,os,sys

def read_files(dir_name):
	# Loop through all files in /Annual Report directory
	for filename in os.listdir(dir_name):
		if filename.endswith(".pdf"):
			response = unirest.post("https://pdf2jpg-pdf2jpg.p.mashape.com/convert_pdf_to_jpg.php",
									headers={"X-Mashape-Key": "TF6tBVGRYSmsh15gqRLOTVMMlsvup1YW6TKjsnha6jaDbQ0yNU"},
									params={"pdf": open(dir_name + filename, mode="r"),
    										"resolution": 150})
			
			# Check response status, and then download converted files
			# print("code",response.code)
			# print(response.headers)
			print(response.body)
			break

if __name__ == '__main__':
	read_files(sys.argv[1])