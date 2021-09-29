import { NextPage } from "next";

import { Container, Box, Spacer, Text, Button } from "@chakra-ui/react";

import MinutesInputForm from "components/pages/submit-form/MinutesInputForm";

const SubmitForm: NextPage = () => {
    return(
        <Container centerContent padding="5">
            <Text fontSize="30">コンピュータ部</Text>
            <Box padding="3">
                <Text textAlign="center">待ち時間</Text>
                <Spacer height="3" />
                <MinutesInputForm />
            </Box>
            <Button colorScheme="teal" margin="4">送信</Button>
        </Container>
    )
}

export default SubmitForm