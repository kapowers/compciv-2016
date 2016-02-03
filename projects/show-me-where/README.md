# Show Me Where Where Durham Susidized Housing Is
# About the dataset
The Durham NC Open Data Portal contains a table of all the subsidized housing accomodations in Durham county. The dataset contains 113 entries. Its fields include location using long/lat, Property Name, Property Address, County, Subsidy End Dates, Total Units, Active Subsidies, Owner, Owner Type.

##Basic Facts about the data set
- The source of the data: [Durham Open Data Initiative, Subsidized Housing](https://opendurham.nc.gov/page/home/)
- The data's landing page: [Subsidized Housing](https://opendurham.nc.gov/explore/dataset/subsidized-housing/table/?dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InN1YnNpZGl6ZWQtaG91c2luZyIsIm9wdGlvbnMiOnt9fSwiY2hhcnRzIjpbeyJ0eXBlIjoibGluZSIsImZ1bmMiOiJBVkciLCJ5QXhpcyI6ImNkIiwiY29sb3IiOiIjNjZjMmE1In1dLCJ4QXhpcyI6InN1YnNpZHlfZW5kX2RhdGUiLCJtYXhwb2ludHMiOiIiLCJ0aW1lc2NhbGUiOiJ5ZWFyIiwic29ydCI6IiJ9XSwidGltZXNjYWxlIjoieWVhciJ9&location=11,35.98433,-78.90557)
- The data form: JSON, CSV, Excel, GeoJSON, Shapefile, KML

## Description of data fields
#### Location 1
Contains a float, in the form of longtitude and latitude: '35.98629037000006, -78.871028600'
#### Property Name
Contains a _text string_ that provides the name of the housing. It is formatted similarly, but some contain different text formatting like capitalized letters.
i.e. 'MURDOCH PLACE' or 'Maplewood Square'
#### Property Address
Contains a _text string_ that is standardized by street number followed by street.
i.e. '206 Gary Street' or '1520 Chapel Hill Road'
####County
Contains a _text string_ that is consistent throughout with 'Durham'
####CD
Contains a _integer_ but it is unclear what it is denoting.
####Subsidy End Date
Contains a _text string_ in the format of MONTH DATE YEAR
i.e. "December 31 2014" 
####Total Units
Contains a _integer_ determinging the total number of units i.e. '1'
####Owner
Contains a _text string_ of the name of the owner with different formatting
i.e. 'MAPLEWOOD PARTNERS LLC' or "QNP Lynnhaven LLC"
####Owner Type
Contains a _text string_ of the type of owner of housing
i.e. 'For Profit' or 'Non-Profit'
## Anticipated data wrangling
I want to compare the locations of non-profit versus profit subsidized housing by their locations using the latitude and longtitude provided.
