"""SQL QUERRIES"""
CREATE_TABLE = (
    """
        CREATE TABLE employee_info(
            EmpID INT NOT NULL,
            EmpFname VARCHAR(255),
            EmpLname VARCHAR(255),
            Department VARCHAR(255),
            Address VARCHAR(255),
            Gender VARCHAR(255)
        )
    """,
    # """
    #     CREATE TABLE EmployeePosition(
    #         EmpID INT,
    #         EmpPosition VARCHAR(255),
    #         DateOfJoining DATE,
    #         Salary INT,
    #         FOREIGN KEY (EmpID) REFERENCES EmployeeInfo(empid)
    #     );
    # """
)

INSERT_DATA = (
    """
        INSERT INTO employee_info \
    (EmpID, EmpFname, EmpLname, Department, Address, Gender) \
    VALUES {}
    """
)

SELECT_ALL = ("select * from {}")
