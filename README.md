### Problem Solving Summary

In this project, we tackled two main problems: searching for foundations using data from 990-PFs and searching for nonprofit salaries using data from 990s and 990 EZs. Below is a summary of how we addressed these challenges:

#### Problem 1: Searching for Foundations (using data from 990-PFs)

**Search Options:**

1. **Geographic Location**: We successfully implemented the ability to search for foundations based on their geographic location.
2. **Grant Application Process**: Information about the grant application process can be found within the Part XV-Supplementary Information section of the 990-PFs.
3. **Recipient of Grant Application**: We identified who should receive grant applications, which can also be located in the Part XV section.
4. **Submission Deadlines**: The submission deadlines for grant applications were successfully extracted.
5. **Restrictions and Limitations**: Information regarding restrictions and limitations on grants was also successfully collected.
6. **Acceptance of Unsolicited Requests**: We identified whether or not the foundation accepts unsolicited requests for funds.

**Types of Grants Provided**: Unfortunately, we encountered a limitation in finding the types of grants provided by foundations. This particular information was not available in the data we processed. Further data or data sources may be necessary to address this aspect.

#### Problem 2: Searching for Nonprofit Salaries (using data from 990s and 990 EZs)

**Search Options:**

1. **Geographic Location**: We successfully implemented the ability to search for nonprofit organizations' salaries based on their geographic location.
2. **Annual Gross Revenue**: Information about annual gross revenue was extracted from Part 1, line 12 for 990s and Part 1, line 9 for 990 EZs.
3. **Annual Net Revenue**: We extracted data related to annual net revenue from Part 1, line 22 for 990s and Part 1, line 21 for 990 EZs.
4. **Job Titles**: We identified job titles containing specific keywords such as "Director," "Chief __ Officer," "Manager," "Coordinator," and "Assistant."

**Average Salary Calculation**: The average salary was calculated by combining the salaries of individuals with various titles, including directors, chief officers, managers, coordinators, and assistants. It's important to note that this calculation may result in some skew towards higher values, as it considers salaries of all employees.