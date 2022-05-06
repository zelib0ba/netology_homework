/* количество исполнителей в каждом жанре:*/
SELECT g.genre_name, COUNT(m.artist_name)
FROM genre AS g
left JOIN genre_artist AS ga ON g.genre_id = ga.genre_id
left JOIN artist AS m ON ga.artist_id = m.artist_id
GROUP BY g.genre_name
ORDER BY COUNT(m.artist_id) DESC;

/*количество треков, вошедших в альбомы 2019-2020 годов:*/
SELECT a.album_name, a.release_year, COUNT(t.track_id)
FROM album AS a
JOIN track AS t ON a.album_id = t.album_id
WHERE a.release_year >= 2019 AND a.release_year <= 2020
GROUP BY a.album_name, a.release_year;

/*средняя продолжительность треков по каждому альбому:*/
SELECT a.album_name, AVG(t.duration)
FROM album AS a
left JOIN track AS t ON t.album_id = a.album_id
GROUP BY a.album_name
ORDER BY AVG(t.duration);

/*все исполнители, которые не выпустили альбомы в 2020 году;*/
SELECT art.artist_name, a.release_year
FROM artist AS art
JOIN artist_album AS aa ON art.artist_id = aa.artist_id
JOIN album AS a ON aa.album_id = a.album_id
WHERE a.release_year != 2020;

/*названия сборников, в которых присутствует конкретный исполнитель (выберите сами);*/
SELECT DISTINCT mc.mcollection_name
FROM mcollection AS mc
JOIN track_collection AS tc ON mc.mcollection_id = tc.mcollection_id
JOIN track AS t ON tc.track_id = t.track_id
JOIN album AS a ON t.album_id = a.album_id
JOIN artist_album AS aa ON a.album_id = aa.album_id
JOIN artist AS art ON aa.artist_id = art.artist_id
WHERE art.artist_name LIKE 'КИНО';
 
/*название альбомов, в которых присутствуют исполнители более 1 жанра;*/
SELECT a.album_name
FROM album AS a /*Albums a*/
JOIN artist_album AS aa ON a.album_id = aa.album_id
JOIN artist AS art ON aa.artist_id = art.artist_id
JOIN genre_artist AS ga ON aa.artist_id = ga.artist_id
GROUP BY art.artist_name, a.album_name
HAVING COUNT(ga.genre_id) > 1;

/*наименование треков, которые не входят в сборники;*/
SELECT t.track_name
FROM track AS t
 LEFT JOIN track_collection AS tc ON t.track_id = tc.track_id
WHERE tc.track_id IS NULL;

/*исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);*/
SELECT art.artist_name, t.duration
FROM artist AS art
JOIN artist_album AS aa ON art.artist_id = aa.artist_id
JOIN album AS a ON aa.album_id = a.album_id
JOIN track AS t ON a.album_id = t.album_id
WHERE t.duration IN (
SELECT MIN(duration)
FROM track);

/*название альбомов, содержащих наименьшее количество треков.*/
SELECT a.album_name, COUNT(t.track_id)
FROM album AS a
JOIN track AS t ON a.album_id = t.album_id
GROUP BY a.album_name
HAVING COUNT(t.track_id) in (
SELECT COUNT(t.track_id)
FROM album AS a
JOIN track AS t ON a.album_id = t.album_id
GROUP BY a.album_name
ORDER BY COUNT(t.track_id)
LIMIT 1)
