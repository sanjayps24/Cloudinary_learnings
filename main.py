import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

from dotenv import load_dotenv
load_dotenv()

# ==============================
# CONFIGURATION
# ==============================
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

# ==============================
# UPLOAD FUNCTION
# ==============================
def upload_file(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    try:
        # Auto-detect resource type (image, video, raw)
        response = cloudinary.uploader.upload(
            file_path,
            resource_type="auto"
        )

        print("\nUpload Successful!")
        print("Public ID:", response.get("public_id"))
        print("URL:", response.get("secure_url"))
        print("Resource Type:", response.get("resource_type"))

    except Exception as e:
        print("Upload Failed:", str(e))


# ==============================
# MAIN
# ==============================
if __name__ == "__main__":
    file_path = r"C:\Users\DELL\Cloudinary_learnings\Toxic_Official_Kannada_Teaser_Rocking_Star_Yash_Geetu_Mohandas_KVN_Monster_Mind_Creations_480P.mp4"
    upload_file(file_path)