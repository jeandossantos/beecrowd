SELECT 
    c1.queue AS queue_id,
    c1.id AS left_chair,
    c2.id AS right_chair
FROM chairs c1
JOIN chairs c2
ON c1.queue = c2.queue
   AND c1.id + 1 = c2.id
   AND c1.available = TRUE
   AND c2.available = TRUE
ORDER BY left_chair;