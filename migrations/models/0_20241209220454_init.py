from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `author` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(120) NOT NULL,
    `age` INT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `publish` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(120) NOT NULL,
    `email` VARCHAR(120) NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `book` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `title` VARCHAR(120) NOT NULL,
    `price` INT NOT NULL,
    `img_url` VARCHAR(250),
    `bread` INT NOT NULL,
    `bcomment` INT NOT NULL,
    `publishs_id` INT NOT NULL,
    CONSTRAINT `fk_book_publish_8999eb74` FOREIGN KEY (`publishs_id`) REFERENCES `publish` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `book_author` (
    `book_id` INT NOT NULL,
    `author_id` INT NOT NULL,
    FOREIGN KEY (`book_id`) REFERENCES `book` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`author_id`) REFERENCES `author` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_book_author_book_id_818352` (`book_id`, `author_id`)
) CHARACTER SET utf8mb4 COMMENT='作者';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
