CREATE DEFINER=`DB_DEVELOPER`@`localhost` PROCEDURE `AddOrEdit`(
IN _name VARCHAR(255),
IN _address VARCHAR(255)
)
BEGIN
IF _name = 0 THEN
INSERT INTO customers(name,address)
VALUES (_name,_address);
SET _name = last_insert_id();
ELSE
UPDATE customers
SET
name = _name,
address = _address
WHERE name = _name;
END IF;
SELECT _name AS 'name';
END