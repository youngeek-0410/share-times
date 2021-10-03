import { NextPage } from 'next'
import React, { useState, useEffect } from 'react'

import { Container, Box, Select, Input, Button, Text } from '@chakra-ui/react'

import { Organization } from 'types/WaitingTimeHistories'
import getOrganizations from './api/getOrganizations'
import requestLogin from './api/requestLogin'

const Login: NextPage = () => {
    const [organizations, setOrganizations] = useState<Organization[]>([])

    const [selectedOrganization, setSelectedOrganization] = useState("")
    const [password, setPassword] = useState<string>("")

    useEffect(() => {
        getOrganizations().then(x => setOrganizations(x))
    }, [])

    const onPasswordInput = (event: React.ChangeEvent<HTMLInputElement>) => {
        setPassword(event.target.value)
    }
    const onOrganizationSelect = (event: React.ChangeEvent<HTMLSelectElement>) => {
        setSelectedOrganization(event.target.value)
    }

    // const login =  () => {
    //     requestLogin(selectedOrganization, password)
    // }

    return (
        <Container centerContent padding="4">
            <Text fontSize="25px">ログイン</Text>
            <Box padding="2">
                <Box paddingBottom="4">
                    <label htmlFor="organization"><Text fontSize="large">展示名</Text></label>
                    <Select id="organization" onChange={onOrganizationSelect} placeholder="選択する">
                        {
                            organizations.map(
                                organization => <option key={organization.uuid} value={organization.name}>{organization.name}</option>
                            )
                        }
                    </Select>
                </Box>
                <Box paddingBottom="4">
                    <label htmlFor="password"><Text fontSize="large">パスワード</Text></label>
                    <Input id="password" onInput={onPasswordInput} placeholder="パスワードを入力" />
                </Box>
            </Box>
            <Button colorScheme="teal" onClick={login}>ログイン</Button>
        </Container>
    )
}

export default Login