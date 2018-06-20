# Music_Video_Bulk_Stream_Download
Streams Music or Video from a file containing list of URL of media, Also download the media which you liked simultaneously 

First generate video/audio URLs from below command or manually add URLs to links.txt file.

youtube-dl --get-url https://www.youtube.com/watch?v=V-mP3VU0DCg&list=PLRBp0Fe2GpgnIh0AiYKh7o7HnYAej-5ph |& tee -a /home/user/Location_of_link_textfile/links.txt
