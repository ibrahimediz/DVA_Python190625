SELECT 
art.Name as ArtistName,
alb.Title as AlbumName,
tr.Name as TrackName
FROM artist as art
LEFT JOIN album as alb ON art.ArtistId = alb.ArtistId
LEFT JOIN track as tr ON alb.AlbumId = tr.AlbumId