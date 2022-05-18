from config import app,client
from flask import request
from producer import messageSender

@app.route('/upload-file',methods=['POST'])
def upload_image():
    bucket='terraformbucket26'
    content_type=request.mimetype
    obj=request.files['file']
    filename=obj.filename
    client.put_object(Body=obj,
          Bucket=bucket,
          Key=filename,
          ContentType=content_type
    )
    msg = f'{filename} sucessfully uploaded'
    messageSender(msg)
    return {'message': 'file uploaded'}, 200

@app.route("/download-file/<string:filename>",methods=["GET"])
def getFileToDownload(filename):
      client.download_file('terraformbucket26',filename,"c:\\new-downloads\\"+filename)
      return {"message ": "check the download folder"}, 200
