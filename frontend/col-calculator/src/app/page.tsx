"use client";
import { Button, Dropdown, Form, Input, Select } from "antd";
import React, { useState } from "react";
import axios from "axios";

const App: React.FC = () => {
  const [form] = Form.useForm();
  const [savings, setSavings] = useState(0);

  const unpackForm = (values) => {
    console.log(values);
    const { salary, state, exemptions, rent, k } = values;
    return getSavings(salary, state, exemptions, rent, k);
  };

  const getSavings = async (
    salary: number,
    state: string,
    exemptions: number,
    rent: number,
    k: number
  ) => {
    const response = await axios.get(
      `http://localhost:8000/savings/${state}/${salary}/${exemptions}/${rent}/${k}`
    );
    console.log(response);
    setSavings(response.data.amount);
  };

  const items = [{ key: "1", label: <div>high</div> }];

  const states = ["California", "Texas"];

  return (
    <>
      <Form
        layout="horizontal"
        form={form}
        onFinish={unpackForm}
        onFinishFailed={() => {
          console.log("Failure!");
        }}
      >
        <Form.Item
          label="Salary"
          rules={[{ required: true, message: "Salary" }]}
          name="salary"
        >
          <Input placeholder="Salary"></Input>
        </Form.Item>

        <Form.Item
          label="State"
          rules={[{ required: true, message: "State" }]}
          name="state"
        >
          <Select>
            {states.map((state: string) => (
              <Select.Option value={state}>{state}</Select.Option>
            ))}
          </Select>
        </Form.Item>
        <Form.Item
          label="Exemptions"
          rules={[{ required: true, message: "Exemptions" }]}
          name="exemptions"
        >
          <Input placeholder="Exemptions"></Input>
        </Form.Item>
        <Form.Item
          label="Rent"
          rules={[{ required: true, message: "Rent" }]}
          name="rent"
        >
          <Select>
            <Select.Option value="low">low</Select.Option>
            <Select.Option value="medium">medium</Select.Option>
            <Select.Option value="high">high</Select.Option>
            <Select.Option value="extreme">extreme</Select.Option>
          </Select>
        </Form.Item>
        <Form.Item
          label="401K"
          rules={[{ required: true, message: "Rent" }]}
          name="k"
        >
          <Input placeholder="401K"></Input>
        </Form.Item>
        <Form.Item rules={[{ required: true, message: "Submit" }]}>
          <Button htmlType="submit">Submit</Button>
        </Form.Item>
      </Form>
      {savings !== 0 && <div>{savings}</div>}
    </>
  );
};

export default App;
