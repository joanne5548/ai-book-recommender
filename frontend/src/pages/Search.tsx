import "../css/search.css";
import { ReactSearchAutocomplete } from "react-search-autocomplete";

const Search = () => {
  type Item = {
    id: number;
    name: string;
  };

  const items = [
    {
      id: 0,
      name: "Cobol",
    },
    {
      id: 1,
      name: "JavaScript",
    },
    {
      id: 2,
      name: "Basic",
    },
    {
      id: 3,
      name: "PHP",
    },
    {
      id: 4,
      name: "Java",
    },
  ];

  const formatResult = (item: Item) => {
    return (
      <>
        <span style={{ display: "block", textAlign: "left" }}>
          id: {item.id}
        </span>
        <span style={{ display: "block", textAlign: "left" }}>
          name: {item.name}
        </span>
      </>
    );
  };

  return (
    <>
      <div className="search-bg-top" />
      <div className="text-center m-5 p-5">
        <p className="search-title">Start Searching</p>
      </div>
      <div id="search-bar">
        <ReactSearchAutocomplete<Item>
          items={items}
          autoFocus
          formatResult={formatResult}
        />
      </div>
      <div className="search-bg-bottom" />
    </>
  );
};

export default Search;
