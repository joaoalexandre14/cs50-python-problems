def main():
    # Ask for file name, remove spaces and ignore case
    filename = input("File name: ").strip().lower()

    # Get extension 
    ext = filename.split(".")[-1]

    # Check extension using if/elif
    if ext == "gif":
        print("image/gif")
    elif ext in ["jpg", "jpeg"]:
        print("image/jpeg")
    elif ext == "png":
        print("image/png")
    elif ext == "pdf":
        print("application/pdf")
    elif ext == "txt":
        print("text/plain")
    elif ext == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
