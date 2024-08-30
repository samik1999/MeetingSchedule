CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE Rooms (
    id INT PRIMARY KEY AUTO_INCREMENT,
    room_name VARCHAR(100) UNIQUE
);

CREATE TABLE Meetings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    start_time DATETIME,
    end_time DATETIME,
    room_id INT,
    creator_id INT,
    FOREIGN KEY (room_id) REFERENCES Rooms(id),
    FOREIGN KEY (creator_id) REFERENCES Users(id)
);

CREATE TABLE Participants (
    meeting_id INT,
    user_id INT,
    FOREIGN KEY (meeting_id) REFERENCES Meetings(id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    PRIMARY KEY (meeting_id, user_id)
);
