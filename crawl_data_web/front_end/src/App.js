import React, { useState } from "react";
import { Table, Input  } from "antd";
import { userColumns } from "./columns";
import { useTableSearch } from "./useTableSearch";
import "antd/dist/antd.css";


const { Search } = Input;

const fetchUsers = async () =>  {
  var data = [];
  await fetch('http://localhost:5000/crawls')
    .then(res => res.json()) 
    .then((datas) => { 
       data = datas.crawls ;
    }) 
  return {data};
};


export default function App() {
  const [searchVal, setSearchVal] = useState(null);

  const { filteredData, loading } = useTableSearch({
    searchVal,
    retrieve: fetchUsers
  });

  return (
    <>
      {/* <h2>CRAWL DATA</h2> */}
      <Search
        onChange={e => setSearchVal(e.target.value)}
        placeholder="Tìm kiếm"
        enterButton
        style={{ position: "sticky",padding: "10px", width: "500px" }}
      />
      <br /> <br />
      <Table 
        rowKey="name"
        dataSource={filteredData}
        columns={userColumns}
        loading={loading}
        pagination={true}
        bordered
      />
    </>
  );
}