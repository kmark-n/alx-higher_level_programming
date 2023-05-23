-- Lists all cities in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT c.id, c.name, s.name FROM cities as c INNER JOIN states as s on c.state_id = s.id ORDER BY c.id;
