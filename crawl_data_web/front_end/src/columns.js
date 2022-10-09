export const userColumns = [
  {
    title: "WebSite",
    dataIndex: "web",
    key: "web"
  },  
  {
      title: "Tên",
      dataIndex: "department",
      key: "department"
  },
  {
      title: "Địa chỉ",
      dataIndex: "address",
      key: "address"
  },
  {
      title: "Loại BĐS",
      dataIndex: "estate",
      key: "estate"
  },
  {
      title: "Giá",
      dataIndex: "price",
      key: "price"
  },
  {
      title: "Diện tích",
      dataIndex: "area",
      key: "area"
  },
  {
      title: "Chi tiết",
      key: "group",
      render: record => {
        return Object.values(record.group)
          .filter(val => typeof val !== "object")
          .join(" , ");
      }
  }
    
  ];
  