def download_data(params):
    import urllib.request
    import zipfile
    import os
    import os.path
    import ssl
    import io
    import pandas as pd

    
    status = {'status': 'False', 'value': None}
    project_parameters = params.get('proj_params', None)
    data_key = params.get('data_key', None)
    print(project_parameters)

    data_url = project_parameters.data_collection_dict[data_key]


    try:
        # Download the ZIP file
        with urllib.request.urlopen(data_url, timeout=15) as response:
            zip_data = response.read()
    except urllib.error.URLError as e:
        print(f"URL error: {e.reason}")
        return None, None, None
    except Exception as e:
        print(f"Download failed: {e}")
        return None, None, None

    try:
        with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
            with z.open("ml-1m/users.dat") as f:
                users = pd.read_csv(f, sep="::", engine="python", header=None, encoding="latin1",
                                    names=['userId','gender','age','occupation','zip-code'])

            with z.open("ml-1m/movies.dat") as f:
                movies = pd.read_csv(f, sep="::", engine="python", header=None, encoding="latin1",
                                     names=['movieId','title','genres'])

            with z.open("ml-1m/ratings.dat") as f:
                ratings = pd.read_csv(f, sep="::", engine="python", header=None, encoding="latin1",
                                      names=['userId','movieId','rating','timestamp'])

        print("✅ MovieLens data loaded successfully.")
        return users, movies, ratings

    except zipfile.BadZipFile:
        print("Error: Not a valid ZIP file.")
    except KeyError as e:
        print(f"Missing file in ZIP: {e}")
    except pd.errors.ParserError as e:
        print(f"Pandas parsing error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return None, None, None
    