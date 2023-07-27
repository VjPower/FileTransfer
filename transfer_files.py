import os
import time 
import pandas as pd 

def transferFiles(source_dir, destination_dir):
    df=pd.DataFrame(columns=['Name','Size','time_for_transfer'])
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    files = os.listdir(source_dir)

    for file in files:
        size=os.path.getsize(f'{source_dir}/{file}')
        
        cur_time=time.time()
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(destination_dir, file)

        os.rename(source_path, destination_path)
        
        final_time=time.time()-cur_time
        print(f"Moved '{file}' to '{destination_dir}'.")

        df=df.append({'Name':file,'Size':size,'time_for_transfer':final_time}, ignore_index=True)
    print(df.to_string())
    df.to_excel('FILE_INFO.xlsx')
    
if __name__ == "__main__":
    source_directory = "/home/viraj/Desktop/GEN_AI/file_dir"  
    destination_directory = "/home/viraj/Desktop/GEN_AI/dest_dir"  

    transferFiles(source_directory, destination_directory)
    
